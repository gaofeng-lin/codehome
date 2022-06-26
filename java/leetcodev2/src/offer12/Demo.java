package offer12;

public class Demo {

    static StringBuilder sb;
    static boolean flag = false;
    public static boolean exist(char[][] board, String word) {
        sb = new StringBuilder();
        boolean[][] visited = new boolean[board.length][board[0].length];
        backtrack(board, word, sb, 0, 0, visited);

        return flag;
    }

    public static void backtrack(char[][] board, String word, StringBuilder sb, int i, int j, boolean[][] visited) {

        if ((sb.toString().equals(word)) ) {
            flag = true;
            return ;
        }

        StringBuilder tmp = new StringBuilder(sb.toString());
        if (tmp.reverse().toString().equals(word)) {
            flag = true;
            return;
        }
        if (i < 0 || i >= board.length || j < 0 || j >= board[0].length || visited[i][j]) {
            return ;
        }



        visited[i][j] = true;
        sb.append(board[i][j]);
        backtrack(board, word, sb, i + 1, j, visited);
        backtrack(board, word, sb, i - 1, j, visited);
        backtrack(board, word, sb, i, j + 1, visited);
        backtrack(board, word, sb, i, j - 1, visited);
        visited[i][j] = false;
        sb.delete(sb.length() - 1, sb.length());

    }

    public static void main(String[] args) {
//        System.out.println("hello");
//        char[][] board = {{'A','B','C','E'},{'S','F','C','S'},{'A','D','E','E'}};
        char[][] board = {{'A','B'}};
        boolean res = exist(board, "BA");
        System.out.println(res);
    }
}
