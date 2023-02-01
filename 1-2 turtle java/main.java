
class la_turtle {
    World w = new World(400, 400);
    Turtle t1 = new Turtle(w);
    Turtle t2 = new Turtle(w);
    int crashes = 0;

    public static void main(String[] args) throws InterruptedException {
        la_turtle my_obj = new la_turtle();

        for (int i = 0; i < Math.random() * 10000; i++) {
            my_obj.t1.moveRandom();
            my_obj.t2.moveRandom();
            my_obj.distance_between(my_obj.t1, my_obj.t2);
            Thread.sleep(30);
        }

        System.out.println("Crashes: " + my_obj.crashes);
    }

    public void distance_between(Turtle t1, Turtle t2) {
        double x1 = t1.getXPos();
        double y1 = t1.getYPos();
        double x2 = t2.getXPos();
        double y2 = t2.getYPos();

        double distance = Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));

        if (distance < 20) {
            crashes++;
            System.out.println("Crash!");
        }
        System.out.println(distance);
    }
}
