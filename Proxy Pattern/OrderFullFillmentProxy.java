import java.util.ArrayList;
import java.util.HashMap;

public class OrderFullFillmentProxy implements OrderInterface {

    private ArrayList<WarehouseReal> warehouses;

    OrderFullFillmentProxy() {
        warehouses = new ArrayList<WarehouseReal>();
    }

    public void addWarehouse(WarehouseReal warehouse) {
        warehouses.add(warehouse);
    }

    @Override
    public void completeOrder(Order order) {

        boolean stock = true;

        for (WarehouseReal warehouse : warehouses) {
            stock = true;

            HashMap<String, Integer> inventory = warehouse.getInventory();

            for (String product : order.cart) {
                if (inventory.get(product) <= 0) {
                    stock = false;
                    break;
                }
            }

            if (stock) {
                warehouse.completeOrder(order);
                break;
            }
        }
        
        if (!stock) {
            System.out.println("Order can't be completed because of Out of stock!!");
        }
    }

}
