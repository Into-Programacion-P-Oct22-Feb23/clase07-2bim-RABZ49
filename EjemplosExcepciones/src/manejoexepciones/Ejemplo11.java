/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package manejoexepciones;

import java.util.InputMismatchException;
import java.util.Scanner;

/**
 *
 * @author reroes
 */
public class Ejemplo11 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        boolean bandera = true;
        String valor;
        while (bandera) {
            try {
                System.out.println("Ingrese valor 1 a operar: ");
                int valor1 = entrada.nextInt(); // 200
                System.out.println("Ingrese valor 2 a operar: ");
                int valor2 = entrada.nextInt(); // 30
                if (valor1 < 0 || valor2 < 0) {
                    throw new Exception("Número negativos");
                }

                if (valor1 > 100) {
                    throw new Exception("El valor de primer valor es muy alto");
                }
                int resultado = valor1 / valor2;
                System.out.printf("Resultado %s\n", resultado);

            } catch (ArithmeticException e) {
                System.out.printf("(ArithmeticException) Ocurrió una "
                        + "excepción %s\n", e);
            } catch (InputMismatchException e) {
                System.out.printf("(InputMismatchException) Ocurrió una "
                        + "excepción %s\n", e);
            } catch (Exception e) {
                System.out.printf("Ocurrió una excepción %s\n", e);
            }
            entrada.nextLine();
            System.out.println("Desea volver a ingresar los valores, ingrese "
                    + "la palabra: si");
            valor = entrada.nextLine(); // no

            if (!valor.equals("si")) { //  Verdadero
                bandera = false;
            }

        }
    }
}
