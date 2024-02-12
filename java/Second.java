import java.util.Scanner;

public class Second {
    // %餘數
    // /整數
    public static void main(String[] args) {
        //給定一個句子，請判斷它是不是迴文，即正著讀或反著讀都一樣的句子。例如:【上海自來水來自海上】是迴文。其他例子:
        //(1) 喜歡的少年是你，你是年少的歡喜
        //(2) 小巷殘月凝天空，親人故土鄉情濃，笑聲猶在空懷舊，憔心客愁滿蒼穹，穹蒼滿愁客心憔，舊懷空在猶聲笑，濃情鄉土故人親，空天凝月殘巷小
        String test = "喜歡的少年是你，你是年少的歡喜";
        boolean palindrome = false;
        for(int i =0;i<test.length()/2;i++) {
            if (test.charAt(i) == test.charAt(test.length() - 1 - i)) {
                palindrome = true;

            }

        }

            if(palindrome){
            System.out.println("是回文");

        }
        else{
            System.out.println("不是回文");
        }




    }
}