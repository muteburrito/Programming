package com.example.information;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;


public class MainActivity extends Activity {

    EditText et;
    Button b;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        b = (Button) findViewById(R.id.next);
        b.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent i = new Intent(getApplicationContext(),NextPage.class);
                et = (EditText) findViewById(R.id.firstName);
                i.putExtra("firstName", et.getText().toString());
                et = (EditText) findViewById(R.id.middleName);
                i.putExtra("middleName", et.getText().toString());
                i.putExtra("lastName", et.getText().toString());
                et = (EditText) findViewById(R.id.email);
                i.putExtra("email", et.getText().toString());
                et = (EditText) findViewById(R.id.birthDate);
                i.putExtra("birthDate", et.getText().toString());
                et = (EditText) findViewById(R.id.address);
                i.putExtra("address", et.getText().toString());
                et = (EditText) findViewById(R.id.mobNo);
                i.putExtra("mobNo", et.getText().toString());
                startActivity(i);
            }
        });
    }
}