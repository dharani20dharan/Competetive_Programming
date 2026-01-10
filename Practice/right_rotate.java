package practice;

import java.util.Arrays;

public class right_rotate {
    public static void main(String[] args) {
        int a[] = {1, 2, 3, 4, 5};
        int n = a.length;
        int k = 2;
        int t[] = new int[n];

        for (int i = 0; i < n; i++) {
            // Formula for right rotation: (current_index + shift) % total_length
            t[(i + k) % n] = a[i];
        }

        System.out.println("Original: " + Arrays.toString(a));
        System.out.println("Rotated:  " + Arrays.toString(t));
    }
}