

class Greeting{
    public static void main(String[] args){
        System.out.println("Good morning!");
        System.out.println("Good evening!");
        System.out.println("Good afternoon!");

        int var = 1;
        System.out.println(var);

        // 整数
        byte var01 = 1;
        short var02 = 12345;
        int var03 = 1234567890;
        long var04 = 123456789000L;

        System.out.println(var01);
        System.out.println(var02);
        System.out.println(var03);
        System.out.println(var04);

        // 少数
        double var05 = 1.23456789;
        double var06 = 1.234F;

        System.out.println(var05);
        System.out.println(var06);

        // 文字
        char var07 = 'c';
        String var08 = "hello,World!";

        System.out.println(var07);
        System.out.println(var08);

        // ブール型
        int var_a = 10;
        int var_b = 1;
        boolean var_bool;

        var_bool = (var_a > var_b);
        System.out.println(var_bool);

        // 配列(ロッカー)の中には要素が含まれる

        String[] arr = {"sato", "suzuki", "tanaka"};

        arr[1] = "nakano";
        System.out.println(arr[0]);
        System.out.println(arr[1]);
        System.out.println(arr[2]);

        String[][] low = {{"sato", "suzuki"},{"tanaka","nakano"}};

        System.out.println(low[0][0]);
        System.out.println(low[0][1]);
        System.out.println(low[1][0]);
        System.out.println(low[1][1]);


        // 算術演算子
        int x = 10;
        int y = 2;

        System.out.println(x+y);
        System.out.println(x-y);
        System.out.println(x*y);
        System.out.println(x/y);
        System.out.println(x%y);

        // 関係演算子
        int z = 10;
        int n = 2;

        System.out.println(z>n);

        // 等価
        int v = 10;
        int b = 2;

        System.out.println(v == b);
        System.out.println(v != b);

        // 論理演算子
        // and＝＆＆
        // or＝｜｜

        // インクリメント 値を1増やす x＋＋
        // デクリメント 値を1減らす x--
        int f = 8;
        int g = 8;

        System.out.println(f++);
        System.out.println(f--);
        










    }
}


