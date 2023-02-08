class person {
    public String name;
    public String surname;
    public int age;

    public void get_name() {
        System.out.println(name + " " + surname);
    }

    public void get_age() {
        System.out.println(age);
    }

    public void increase_age() {
        age++;
    }

    public void get_days() {
        System.out.println(age * 365);
    }

    public void get_all() {
        System.out.println(name + " " + surname + " is " + age + " years old which equals " + (age * 365) + " days.");
    }
}

class main {
    public static void main(String[] args) {
        person p1 = new person();
        p1.name = "John";
        p1.surname = "Doe";
        p1.age = 20;

        person p2 = new person();
        p2.name = "Jane";
        p2.surname = "Doe";
        p2.age = 18;

        p1.get_name();
        p1.get_age();
        p1.increase_age();
        p1.get_age();
        p1.get_days();
        p1.get_all();

        p2.get_name();
        p2.get_age();
        p2.increase_age();
        p2.get_age();
        p2.get_days();
        p2.get_all();
    }
}
