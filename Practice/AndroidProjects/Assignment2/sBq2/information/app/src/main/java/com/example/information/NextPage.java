package com.example.information;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class NextPage extends Activity {

    TextView tv;
    Button b;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_next_page);
        Intent i = getIntent();
        tv = (TextView)findViewById(R.id.firstName);
        tv.setText("First Name : "+i.getStringExtra("firstName"));

        tv = (TextView)findViewById(R.id.middleName);
        tv.setText("Middle Name : "+i.getStringExtra("middleName"));

        tv = (TextView)findViewById(R.id.lastName);
        tv.setText("Last Name : "+i.getStringExtra("lastName"));

        tv = (TextView)findViewById(R.id.email);
        tv.setText("Email : "+i.getStringExtra("email"));

        tv = (TextView)findViewById(R.id.address);
        tv.setText("Address : "+i.getStringExtra("address"));

        tv = (TextView)findViewById(R.id.birthDate);
        tv.setText("Date of Birth : "+i.getStringExtra("birthDate"));

        tv = (TextView)findViewById(R.id.mobNo);
        tv.setText("Mobile No.  : "+i.getStringExtra("mobNo"));

        b = (Button)findViewById(R.id.back);
        b.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent i = new Intent(getApplicationContext(),MainActivity.class);
                startActivity(i);
            }
        });

    }
}