public class HolaDocker {

    public static void main(String[] args) {
		System.out.println("Número de argumentos: " + args.length);
        System.out.println("Hola desde Java dentro de Docker "+args[0]);
    }
}