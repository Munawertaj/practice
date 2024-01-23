public class AuthenticatedWebpage extends WebpageDecorator {

    AuthenticatedWebpage(Webpage webpage) {
        super(webpage);
    }

    public void AuthenticatedWebpage() {
        System.out.println("Authenticating User....");
    }

    public void display() {
        this.AuthenticatedWebpage();
        super.display();
    }

}
