package com.example.goodmorning;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        TextView text;
        EditText n1, n2;
        Button button;
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toast.makeText(this, "Good Morning", Toast.LENGTH_SHORT).show();
        text = findViewById(R.id.text);
        text.setText("Good Morning");
        n1 = findViewById(R.id.num1);
        n2 = findViewById(R.id.num2);
        button = findViewById(R.id.button);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                int sum = Integer.parseInt(n1.getText().toString()) + Integer.parseInt(n2.getText().toString());
                text.setText("The sum is: "+sum);
            }
        });

    }
}