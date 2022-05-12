package com.example.spinner;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {


    Spinner spinner;
    Button add,remove;
    EditText et;
    ArrayList item;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        spinner = (Spinner)findViewById(R.id.spinner);
        item = new ArrayList();
        item.add("Apple");
        add = (Button) findViewById(R.id.add);
        remove = (Button) findViewById(R.id.remove);
        et = (EditText) findViewById(R.id.input);

        ArrayAdapter data = new ArrayAdapter(MainActivity.this, android.R.layout.simple_spinner_item,item);
        data.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner.setAdapter(data);

    }
}