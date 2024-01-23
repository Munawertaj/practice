import java.util.ArrayList;

public class Order {

    ArrayList<String> cart = new ArrayList<>();

    public void addToCart(String item) {
        cart.add(item);
    }
}
