# Projeto-para-Faculdade-Miss-o-pratica-4-Calculadora-Orientada-a-Objetos-usando-Python-
Missão Prática | Conhecendo novos
paradigmas 💻

Após aplicar, de forma prática, os conceitos básicos de Programação Orientada a
Objetos usando Python, chegou a hora de refatorar um código, inicialmente
escrito, em outras microatividades, com uso do paradigma de Programação
Estruturada.

Contextualização

Como aluno do curso de Desenvolvimento de Sistemas, você construiu, ao longo
das primeiras disciplinas, um programa para simular uma calculadora simples,
que permite a entrada de dados pelo usuário, a escolha da operação matemática
a ser executada e a exibição do resultado da conta ao final. Agora, tendo visto os
conceitos de OO, chegou a hora de refatorar os códigos da sua calculadora. Para
isso, siga os procedimentos descritos a seguir.

Roteiro de prática 📝

- Material necessário para a prática

Interpretador Python instalado no Sistema Operacional;
IDE VS Code instalada no Sistema Operacional;
 

- Procedimentos

1.      Abra a IDE VS Code;

2.      Na mesma pasta onde criou os scripts utilizados nas microatividades, crie
dois novos scripts chamados “Calculadora.py” e “main_calculadora.py”,
respectivamente;

3.      No script “Calculadora”:

a.      Crie uma classe chamada Calculadora;

b.      Defina os seguintes atributos privados para essa classe:

valorA;
valorB;
operação
c.      Defina os métodos “getters” e “setters” para os atributos, usando
@property;

d.      Crie um método chamado “validarOperacao”. Esse método receberá como
parâmetro o símbolo da operação matemática a ser executada. Caso o símbolo
passado não seja válido/não exista, esse método deverá retornar False. Do
contrário, retornará True;

e.      Crie um método chamado “calcular”. Esse método não receberá
parâmetros. Em seu escopo, esse método deverá:

Verificar o valor atribuído para o atributo “operacao” usando o método
“validarOperacao”. Caso a operação não seja válida, deverá ser impressa,
na tela, uma mensagem e o programa deverá ser encerrado
imediatamente. Do contrário, o método deverá verificar a operação
definida e retornar o respectivo cálculo;
 Caso a operação selecionada seja a de divisão, deverá ser verificado se o
valor de um dos parâmetros é igual a 0. Em caso positivo, deverá ser
impressa, na tela, uma mensagem informando não ser possível realizar tal
operação. Além disso, o programa deverá ser encerrado imediatamente.
f.       Crie um método chamado “mostrarResultado”. Esse método não deverá
receber parâmetro e servirá para exibir, na tela, os valores dos atributos valorA,
valorB e operação:

 

print(str(self.valorA) + ' ' + self.operacao + ' ' + str(self.valorB) + ' = ' +
str(self.calcular()))

g.      Salve as alterações realizadas.

 

4.      No script “main_calculadora”:

Importe a classe Calculadora;
Crie uma nova instância da classe, passando os valores e a operação a ser
realizada;
Realize a chamada do método “mostrarResultado”.
Salve as alterações no script e execute o script via VS Code;
Conforme executar com sucesso, altere os valores passados como
argumentos, testando diferentes combinações, assim como as verificações
implementadas.
5.      Para aprimorar sua Calculadora, você poderá, ainda, implementar um
método na classe Calculadora que permita a entrada de dados via prompt. Com
isso, você deverá também alterar a criação da instância da classe, para que
utilize os valores passados pelo usuário e não valores setados diretamente no
código.

- Resultados esperados  ✨

O resultado esperado dessa atividade é permitir ao aluno, de forma consolidade e
através de um exemplo prático, aplicar os conhecimentos de OO vistos ao longo
das microatividades.
