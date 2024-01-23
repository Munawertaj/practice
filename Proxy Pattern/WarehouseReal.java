import java.util.HashMap;

public class WarehouseReal implements OrderInterface {

    private HashMap<String, Integer> inventory;

    WarehouseReal() {
        inventory = new HashMap<String, Integer>();
    }

    @Override
    public void completeOrder(Order order) {
        for (String product : order.cart) {
            int amount = inventory.get(product);
            inventory.put(product, amount - 1);
        }
        System.out.println("Order is completed successfully...");
    }

    public void addToInventory(String product, int amount) {
        inventory.put(product, amount);
    }

    public HashMap<String, Integer> getInventory() {
        return this.inventory;
    }

}
