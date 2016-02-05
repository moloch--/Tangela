import com.sun.java.browser.dom.*;
import java.applet.Applet;
import java.awt.*;
import org.w3c.dom.html.*;

public class TitleTester extends Applet {
  private String title = "Test error";

  public void init () {

    try {

      DOMService svc = DOMService.getService(this);

      title = (String) svc.invokeAndWait (
        new DOMAction () {
          public Object run (DOMAccessor acc) {
            try {
              HTMLDocument doc = (HTMLDocument) acc.getDocument(TitleTester.this);
              return doc.getTitle();
            } catch (Exception e) { }
            return "DOMService not supported (2).";
          }
        }
      );

    } catch (DOMAccessException e) { title = "Permission denied."; }
      catch (Exception e) { title = "DOMService not supported (1)."; }

  }

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
