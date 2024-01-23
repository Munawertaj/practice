public class AuthorizationWebpage extends WebpageDecorator {

    AuthorizationWebpage(Webpage webpage) {
        super(webpage);
    }

    public void AuthorizationWebpage() {
        System.out.println("Authorization User....");
    }

    public void display() {
        this.AuthorizationWebpage();
        super.display();
    }

}
