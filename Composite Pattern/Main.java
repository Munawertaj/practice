public class Main {
    public static void main(String[] args) {
        Housing wazedMia = new Housing("4th Science Building");

        Housing department1 = new Housing("CSE");

        Room room1 = new Room("Seminar Library");
        Room room2 = new Room("ICT Center");
        Room room3 = new Room("AR VR Lab");

        department1.addComponent(room1);
        department1.addComponent(room2);
        department1.addComponent(room3);

        Housing department2 = new Housing("Pharmacy");

        Room room4 = new Room("Washroom");
        Room room5 = new Room("Chemical Lab");

        department2.addComponent(room4);
        department2.addComponent(room5);

        wazedMia.addComponent(department1);
        wazedMia.addComponent(department2);

        wazedMia.enter();
        wazedMia.location();
        
        department1.enter();
        department1.location();
        
        room1.enter();
        room1.location();
        room1.exit();

        department1.exit();

        department2.enter();
        department2.location();

        room5.enter();
        room5.location();
        room5.exit();

        department2.exit();

        wazedMia.exit();

    }
}
