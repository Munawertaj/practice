import java.util.ArrayList;

class FosterHome {
    private String fosterHomeName;
    private ArrayList<Pet> pets;
    private ArrayList<Pet> adoptedPets;
    private ArrayList<Pet> rescuedPets;
    private ArrayList<Pet> adoptionPets;

    public FosterHome(String fosterHomeName) {

        this.fosterHomeName = fosterHomeName;
        this.pets = new ArrayList<>();
        this.adoptedPets = new ArrayList<>();
        this.adoptionPets = new ArrayList<>();
        this.rescuedPets = new ArrayList<>();
    }

    public void addPet(Pet pet) {
        pets.add(pet);
        System.out.println(pet.getPetName() + " (" + pet.getPetSpecies() + ") has been added to " + fosterHomeName);
    }

    public void displayPets() {
        System.out.println("Pets in " + fosterHomeName + ":");
        for (Pet pet : pets) {
            System.out.println("-> " + pet.getPetName() + " (" + pet.getPetSpecies() + ")");
        }
    }

    public void rescuePet(Pet pet) {
        rescuedPets.add(pet);
        System.out.println(pet.getPetName() + " (" + pet.getPetSpecies() +  ") has been rescued in " + fosterHomeName);
    }

    public void displayRescuedPets() {
        System.out.println("Rescued Pets in " + fosterHomeName + " are :");
        for (Pet pet : rescuedPets) {
            System.out.println("-> " + pet.getPetName() + " (" + pet.getPetSpecies() + ")");
        }
    }

    public void addPetForAdoption(Pet pet) {
        adoptionPets.add(pet);
        System.out.println(pet.getPetName() + " (" + pet.getPetSpecies()  + ") is now available for adaption in " + fosterHomeName);
    }

    public void displayAdoptionPets() {
        System.out.println("Pets for adoption in " + fosterHomeName + " are :");
        for (Pet pet : adoptionPets) {
            System.out.println("-> " + pet.getPetName() + " (" + pet.getPetSpecies() + ")");
        }
    }

    public void adoptPet(Pet pet) {
        adoptedPets.add(pet);
        adoptionPets.remove(pet);
        System.out.println(pet.getPetName() + " (" + pet.getPetSpecies() + ")" + " has been adopted in " + fosterHomeName);
    }

    public void displayAdoptedPets() {
        System.out.println("Pets have been adapted here in " + fosterHomeName + " are :");
        for (Pet pet : adoptedPets) {
            System.out.println("-> " + pet.getPetName() + " (" + pet.getPetSpecies() + ")");
        }
    }
}
