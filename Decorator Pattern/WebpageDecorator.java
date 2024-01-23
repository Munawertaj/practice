public class WebpageDecorator implements Webpage {

    Webpage webpage;

    WebpageDecorator(Webpage webpage) {
        this.webpage = webpage;
    }

    @Override
    public void display() {
        this.webpage.display();
    }

}
