import java.net.*;
import java.io.*;
import com.sun.java.browser.dom.*;
import java.applet.Applet;
import java.awt.*;
import org.w3c.dom.html.*;

public class HttpOnlyTester extends Applet {
  private String result = "Test error";

  public void init () {

    try {
 
      String location = "http://[SERVER_NAME]/[SERVER_PATH]/.set_httponly.php";
      URL servlet = new URL( location );
      URLConnection conn = servlet.openConnection(); 
      BufferedReader in = new BufferedReader( new InputStreamReader( conn.getInputStream() ) );

      for (int i=0;i<64;i++) {

        if (conn.getHeaderField(i) == null) {
          result = "HttpOnly cookie HIDDEN from Java (" + i + ")";
          break;
        }

        if (conn.getHeaderField(i).indexOf("HTTP_ONLY_COOKIE") != -1) {
          result = "HttpOnly cookie seen by Java";
          break;
        }
      }

   
     } catch (java.net.MalformedURLException e) { }
       catch (java.io.IOException e) { }

   }


  public void paint (Graphics g) {
    int width = getSize ().width;
    int height = getSize ().height;

    g.setColor (Color.cyan);
    g.fillRect (0, 0, width, height);

    FontMetrics fm = g.getFontMetrics ();

    g.setColor (Color.black);
    g.drawString (result, (width-fm.stringWidth (result))/2, height/2);
  }

}
