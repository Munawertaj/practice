public class Main {
    public static void main(String[] args) {

        Webpage myWebpage = new BasicWebPage("HTML", "CSS", "JAVASCRIPT");
        myWebpage = new AuthenticatedWebpage(myWebpage);
        myWebpage = new AuthorizationWebpage(myWebpage);
        myWebpage.display();
    }
    
}
