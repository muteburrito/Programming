package com.example.addition;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    EditText no1,no2;
    Button add;
    TextView result;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        no1 = (EditText) findViewById(R.id.no1);
        no2 = (EditText) findViewById(R.id.no2);
        add = (Button) findViewById(R.id.addition);
        result = (TextView) findViewById(R.id.result);
        add.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                double n1 = Double.parseDouble(no1.getText().toString());
                double n2 = Double.parseDouble(no2.getText().toString());
                double sum = n1+n2;
                result.setText(Double.toString(sum));
            }
        });
    }
}