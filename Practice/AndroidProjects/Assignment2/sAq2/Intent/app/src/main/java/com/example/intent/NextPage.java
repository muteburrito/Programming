package com.example.intent;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class NextPage extends AppCompatActivity {

    Button button;
    TextView tv;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_next_page2);
        button = (Button) findViewById(R.id.back);
        tv=(TextView) findViewById(R.id.output);

        Intent i = getIntent();
        Bundle b = i.getExtras();
        String output = b.get("msg").toString();
        tv.setText(output);

    }
    public void Pre(View view) {
        Intent i = new Intent(getApplicationContext(),MainActivity.class);
        startActivity(i);
    }
}