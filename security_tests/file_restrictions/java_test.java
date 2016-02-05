import com.sun.java.browser.dom.*;
import java.applet.Applet;
import java.awt.*;
import org.w3c.dom.html.*;

public class java_test extends Applet {
  private String title = "HELLO WORLD";

  public void init () { }

  public void paint (Graphics g) {
    int width = getSize ().width;
    int height = getSize ().height;

    g.setColor (Color.cyan);
    g.fillRect (0, 0, width, height);

    FontMetrics fm = g.getFontMetrics ();

    g.setColor (Color.black);
    g.drawString (title, (width-fm.stringWidth (title))/2, height/2);
 }

}
