package com.example.contact;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.telephony.SmsManager;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.Toast;

public class Details extends AppCompatActivity {

    EditText et;
    ImageButton call1, call2, msg;
    Button create, update, insert;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_details);
        et = (EditText) findViewById(R.id.number);
        create = (Button) findViewById(R.id.createContact);
        update = (Button) findViewById(R.id.update);
        insert = (Button) findViewById(R.id.InsertRecord);
        call1 = (ImageButton) findViewById(R.id.call);
        call2 = (ImageButton) findViewById(R.id.call2);
        msg = (ImageButton) findViewById(R.id.msg);
        insert.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Toast.makeText(Details.this, "Record Inserted Successfully ", Toast.LENGTH_SHORT).show();
            }
        });
    }
}
