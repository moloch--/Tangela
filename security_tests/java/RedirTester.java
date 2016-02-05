import java.net.*;
import java.io.*;
import com.sun.java.browser.dom.*;
import java.applet.Applet;
import java.awt.*;
import org.w3c.dom.html.*;

public class RedirTester extends Applet {
  private String result = "Cross-domain redirects not visible to Java";

  public void init () {

    try {
 
      String location = "http://[SERVER_NAME]/[SERVER_PATH]/.redir_ext.php";
      URL servlet = new URL( location );
      URLConnection conn = servlet.openConnection(); 
      BufferedReader in = new BufferedReader( new InputStreamReader( conn.getInputStream() ) );

      for (int i=0;i<64;i++) {

        if (conn.getHeaderField(i) == null) {
          break;
        }

        if (conn.getHeaderField(i).indexOf("RESPONSE_VISIBILITY_TEST") != -1) {
          result = "Cross-domain redirects VISIBLE to Java";
          break;
        }
      }

   
     } catch (Exception e) { }

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
