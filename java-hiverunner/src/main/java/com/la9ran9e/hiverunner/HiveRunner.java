package com.la9ran9e.hiverunner;

import com.google.common.base.Joiner;
import com.klarna.hiverunner.HiveServerContainer;
import com.klarna.hiverunner.StandaloneHiveServerContext;
import com.klarna.hiverunner.config.HiveRunnerConfig;
import org.apache.commons.io.FileUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;


public class HiveRunner {

    private static final Logger LOGGER = LoggerFactory.getLogger(HiveRunner.class);

    private final String basedirPrefix;
    private Path basedir;
    private HiveServerContainer container;
    private static final String DEFAULT_NULL_REPRESENTATION = "NULL";
    private static final String DEFAULT_ROW_VALUE_DELIMTER = "\t";

    public HiveRunner() { this("hiverunner-"); }

    public HiveRunner(String basedirPrefix) { this.basedirPrefix = basedirPrefix; }

    public void setup() throws IOException {
        basedir = Files.createTempDirectory(basedirPrefix);
        StandaloneHiveServerContext context = new StandaloneHiveServerContext(basedir, new HiveRunnerConfig());
        container = new HiveServerContainer(context);
        container.init(new HashMap<String, String>(), new HashMap<String, String>());
    }

    public void stop() {
        tearDown();
    }

    public List<String> executeQuery(String query) {
        return executeQuery(query, DEFAULT_ROW_VALUE_DELIMTER, DEFAULT_NULL_REPRESENTATION);
    }

    public List<String> executeQuery(String query, String rowValuesDelimitedBy, String replaceNullWith) {
        List<Object[]> resultSet = container.executeStatement(query);
        List<String> result = new ArrayList<String>();
        for (Object[] objects : resultSet) {
            result.add(Joiner.on(rowValuesDelimitedBy).useForNull(replaceNullWith).join(objects));
        }
        return result;
    }

    private void tearDown() {
        if (container != null) {
            LOGGER.info("Tearing down");
            container.tearDown();
        }
        deleteTempFolder(basedir);
    }

    private void deleteTempFolder(Path directory) {
        try {
            FileUtils.deleteDirectory(directory.toFile());
        } catch (IOException e) {
            LOGGER.debug("Temporary folder was not deleted successfully: " + directory);
        }
    }
}
