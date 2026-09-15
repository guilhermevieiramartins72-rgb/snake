//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
void main() {
    String nome;
    byte idade;
    String algo;

    Scanner entradausuario = new Scanner(System.in);

    System.out.println("Qual seu nome?");
    nome = entradausuario.nextLine();
    System.out.println( " qual sua idade? ");
    idade = entradausuario.nextByte();
    System.out.println("Qual sua profissao? ");
    algo = entradausuario.nextLine();


    System.out.println("Meu nome é "+ nome + ", tenho "+ idade+ " e sou " + algo);


}





