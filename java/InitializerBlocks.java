import java.util.Arrays;

public class InitializerBlocks
{
    private static void LOG(String msg, Object... args)
    {
        StackTraceElement ste = Thread.currentThread().getStackTrace()[3];
        String className = ste.getClassName();
        className = className.substring(className.indexOf('$') + 1);
        System.out.println("[(" + ste.getFileName() + ":"
                                + ste.getLineNumber() + ") "
                             + className + "] "
                             + msg + " " + Arrays.toString(args));
    }

    /**
     * Super class!
     */
    public static class Super
    {
        static {
            LOG("Static Initializer Block 1");
        }

        {
            LOG("Instance Initializer Block 1");
        }

        public Super()
        {
            LOG("Default CTOR");
        }

        static {
            LOG("Static Initializer Block 2");
        }

        {
            LOG("Instance Initializer Block 2");
        }

        public Super(int i)
        {
            LOG("CTOR", i);
        }

        public Super(int i, double d)
        {
            LOG("CTOR", i, d);
        }

        public Super(int i, double d, boolean b)
        {
            this(i);
            LOG("CTOR", i, d, b);
        }

        public Super(int i, double d, boolean b, char c)
        {
            this(i, d);
            LOG("CTOR", i, d, b, c);
        }
    }

    /**
     * And its Sub class!
     */
    public static class Sub extends Super
    {
        static {
            LOG("Static Initializer Block 1");
        }

        {
            LOG("Instance Initializer Block 1");
        }

        public Sub(int i)
        {
            LOG("CTOR", i);
        }

        {
            LOG("Instance Initializer Block 1");
        }

        static {
            LOG("Static Initializer Block 2");
        }

        public Sub(int i, double d)
        {
            super(i, d);
            LOG("CTOR", i, d);
        }

        public Sub(int i, double d, boolean b)
        {
            this(i, d);
            LOG("CTOR", i, d);
        }

        public Sub(int i, double d, boolean b, char c)
        {
            super(i, d, b, c);
            LOG("CTOR", i, d, b, c);
        }
    }

    public static void main(String... args)
    {
        Super s = new Super();
        System.out.println("---------------");
        Super s1 = new Super(42);
        System.out.println("---------------");
        Super s2 = new Super(10, 3.14159);
        System.out.println("---------------");
        Super s3 = new Super(99, 2.71828, true);
        System.out.println("---------------");
        Super s4 = new Super(99, 2.71828, true, '$');
        System.out.println("---------------");

        Sub sub = new Sub(1);
        System.out.println("---------------");
        Sub sub2 = new Sub(2, 3.0);
        System.out.println("---------------");
        Sub sub3 = new Sub(4, 5.0, true);
        System.out.println("---------------");
        Sub sub4 = new Sub(6, 7.0, true, '@');
        System.out.println("---------------");
    }
}
