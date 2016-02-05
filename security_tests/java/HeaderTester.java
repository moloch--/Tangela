import java.net.*;
import java.io.*;
import com.sun.java.browser.dom.*;
import java.applet.Applet;
import java.awt.*;
import org.w3c.dom.html.*;

public class HeaderTester extends Applet {
  private String can_set = "Can set: ";
  private String cant_set = "Can't set: ";
  private String except = "Exceptions: ";

  private void test_header(String val) {
    String location = "http://[SERVER_NAME]/[SERVER_PATH]/.read_header.php?" + val.toUpperCase().replace('-','_');

    try {
 
      URL servlet = new URL( location );
      URLConnection conn = servlet.openConnection(); 
      conn.setRequestProperty(val,"JAVA_TEST");
      BufferedReader in = new BufferedReader( new InputStreamReader( conn.getInputStream() ) );

      if (in.readLine().indexOf("JAVA_TEST") != -1)
        can_set += " " + val;
      else
        cant_set += " " + val;
   
     } catch (Exception e) { except += " " + val; }

  }

  public void init() {
    test_header("Accept");
    test_header("Accept-Charset");
    test_header("Accept-Encoding");
    test_header("Accept-Language");
    test_header("Cache-Control");
    test_header("Cookie");
    test_header("Host");
    test_header("If-Match");
    test_header("If-Modified-Since");
    test_header("If-None-Match");
    test_header("If-Range");
    test_header("If-Unmodified-Since");
    test_header("Range");
    test_header("Transfer-Encoding");
    test_header("User-Agent");
    test_header("Vary");
    test_header("Via");
    test_header("X-Arbitrary-Header-Field");
  }

  public void paint (Graphics g) {
    int width = getSize ().width;
    int height = getSize ().height;

    g.setColor (Color.cyan);
    g.fillRect (0, 0, width, height);

    FontMetrics fm = g.getFontMetrics ();

    g.setColor (Color.black);
    g.drawString (can_set, 10, 20);
    g.drawString (cant_set, 10, 50);
    g.drawString (except, 10, 80);

  }

}
