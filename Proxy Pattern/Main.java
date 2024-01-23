public class Main {

    public static void main(String[] args) {
        Order myOrder = new Order();

        myOrder.addToCart("Book");
        myOrder.addToCart("Laptop");
        myOrder.addToCart("Smartphone");

        OrderFullFillmentProxy orderFullFillment = new OrderFullFillmentProxy();

        WarehouseReal warehouse1 = new WarehouseReal();
        WarehouseReal warehouse2 = new WarehouseReal();

        warehouse1.addToInventory("Laptop", 5);
        warehouse1.addToInventory("Smartphone", 10);
        warehouse1.addToInventory("Book", 5);

        orderFullFillment.addWarehouse(warehouse1);
        orderFullFillment.addWarehouse(warehouse2);

        orderFullFillment.completeOrder(myOrder);

    }
}
