package com.example.intent;

import androidx.appcompat.app.AppCompatActivity;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {

    Button b;
    EditText ed;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        b = (Button) findViewById(R.id.button);
        ed = (EditText) findViewById(R.id.msg);
    }
    public void Next(View view) {
        Intent i = new Intent(getApplicationContext(),NextPage.class);
//        ed.getText().toString();
        i.putExtra("msg",ed.getText().toString());
        startActivity(i);
    }

}

