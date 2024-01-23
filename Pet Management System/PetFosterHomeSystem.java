public class PetFosterHomeSystem {
    public static void main(String[] args) {

        FosterHome fosterHome1 = new FosterHome("Pet Care BD");

        Pet pet1 = new Pet("Hamba", "Cat");
        Pet pet2 = new Pet("Puchi", "Cat");
        Pet pet3 = new Pet("Fiona", "Cat");
        Pet pet4 = new Pet("Tommy", "Dog");
        Pet pet5 = new Pet("Mukku", "Dog");

        fosterHome1.addPet(pet1);
        fosterHome1.addPet(pet2);

        fosterHome1.displayPets();

        fosterHome1.rescuePet(pet3);
        fosterHome1.rescuePet(pet4);
        fosterHome1.rescuePet(pet5);

        fosterHome1.displayRescuedPets();

    }
}