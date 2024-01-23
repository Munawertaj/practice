public class BasicWebPage implements Webpage {

    private String html;
    private String css;
    private String js;

    BasicWebPage(String html, String css, String js) {
        this.html = html;
        this.css = css;
        this.js = js;
    }

    @Override
    public void display() {
        System.out.println("Basic Web Page:");
        System.out.println("HTML: " + html);
        System.out.println("Stylesheet: " + css);
        System.out.println("Script: " + js);
    }

}
