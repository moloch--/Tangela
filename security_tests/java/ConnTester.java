import java.net.*;
import java.io.*;
import com.sun.java.browser.dom.*;
import java.applet.Applet;
import java.awt.*;
import org.w3c.dom.html.*;

public class ConnTester extends Applet {
  private String result = "Test error";

  public void init () {

    try {
 
      String location = "http://[SERVER_NAME]/[SERVER_PATH]/.read_header.php?COOKIE";
      URL servlet = new URL( location );
      URLConnection conn = servlet.openConnection(); 
      BufferedReader in = new BufferedReader( new InputStreamReader( conn.getInputStream() ) );

      if (in.readLine().indexOf("JAVA_COOKIE_TEST") != -1)
        result = "Browser stack used (browser cookies seen)";
      else
        result = "Separate stack used (or browser cookies off)";
   
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
