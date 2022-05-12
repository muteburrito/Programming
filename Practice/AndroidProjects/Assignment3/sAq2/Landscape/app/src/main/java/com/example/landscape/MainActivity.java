package com.example.landscape;

import androidx.appcompat.app.AppCompatActivity;

import android.graphics.Color;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    EditText et;
    RadioButton r1,r2;
    TextView tv;
    Button b;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        et = (EditText) findViewById(R.id.input);
        tv = (TextView) findViewById(R.id.output);
        r1 = (RadioButton) findViewById(R.id.YtoM);
        r2 = (RadioButton) findViewById(R.id.MtoY);
        b = (Button) findViewById(R.id.button);

        r1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                r2.setChecked(false);
            }
        });

        r2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                r1.setChecked(false);
            }
        });

    }

    public void result(View view){
        if (et.getText().toString().isEmpty()) {
            tv.setText("Enter a Rate of Interest");
            tv.setTextColor(Color.RED);
        }else {
            Double rate = Double.parseDouble(et.getText().toString());
            Double convert;
            if (r1.isChecked()) {
                convert = rate / 12;
            } else  {
                convert = rate * 12;
            }
            tv.setTextColor(Color.BLACK);
            tv.setText("Converted Rate is : " + convert);
        }
    }
}