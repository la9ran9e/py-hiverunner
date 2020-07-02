import py4j.GatewayServer;

import com.la9ran9e.hiverunner.HiveRunner;

import java.net.Inet4Address;
import java.net.InetAddress;
import java.net.UnknownHostException;

public class HiveRunnerEntryPoint {

    public HiveRunner getHiveRunnerInstance (String basedirPrefix) {
        return new HiveRunner(basedirPrefix);
    }

    public static void main(String[] args) throws UnknownHostException {
        InetAddress addr;
        System.setProperty("java.net.preferIPv4Stack", "true");
        addr = Inet4Address.getByName("0.0.0.0");
        GatewayServer.GatewayServerBuilder builder = new GatewayServer.GatewayServerBuilder(new HiveRunnerEntryPoint());
        builder.javaAddress(addr);
        GatewayServer server = builder.build();
        server.start();
        System.out.println("Gateway Server Started");
    }

}
