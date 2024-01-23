public class Person implements Playing, Swimming, Walking {

    private String name;

    public Person(String name) {
        this.name = name;
    }

    @Override
    public void play() {
        System.out.println(name + " is playing.");
    }

    @Override
    public void walk() {
        System.out.println(name + " is walking.");
    }

    @Override
    public void swim() {
        System.out.println(name + " is swimming.");
    }
}
