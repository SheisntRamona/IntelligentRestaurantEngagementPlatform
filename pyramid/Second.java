import java.sql.SQLOutput;
import java.util.Scanner;

public class Second {
    // %餘數
    // /整數

    public static void  printStars(int space,int star){
        String result="";
        for(int j=0;j<space;j++){
            result +=" ";
        }


        for(int i=0;i<star;i++){
            result += "*";



        }
        System.out.println(result);
    }
    public static void pyramid(int n){
        int stars=2*n-1;
        int space=0;
        while (stars>0){
            printStars(space,stars);
            space++;
            stars-=2;
        }

    }





    public static void main(String[] args) {
        pyramid(1);
        System.out.println("====================");
        pyramid(3);
        System.out.println("====================");
        pyramid(5);
    }
}








