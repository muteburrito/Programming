package com.example.loginpage;
import androidx.appcompat.app.AppCompatActivity;

import android.app.Activity;
import android.content.Intent;
import android.graphics.Color;
import android.os.Bundle;
import android.text.method.LinkMovementMethod;
import android.text.util.Linkify;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import java.util.regex.Pattern;

public class MainActivity extends Activity {

    Button b;
    EditText email, password;
    TextView tv;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        b = (Button) findViewById(R.id.button);
        email = (EditText) findViewById(R.id.email);
        password = (EditText) findViewById(R.id.password);
        b.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (email.getText().toString().equals("Admin") && !password.getText().toString().equals("Password")) {
                    Intent i = new Intent(getApplicationContext(), NextPage.class);
                    startActivity(i);
                } else
                    Toast.makeText(MainActivity.this, "COMPLETE ALL THE FIELDS", Toast.LENGTH_SHORT).show();
            }
        });
    }

}