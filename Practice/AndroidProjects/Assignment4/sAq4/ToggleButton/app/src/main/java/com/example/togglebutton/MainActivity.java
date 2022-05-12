package com.example.togglebutton;

import androidx.appcompat.app.AppCompatActivity;

import android.app.Activity;
import android.content.Context;
import android.content.pm.PackageManager;
import android.hardware.camera2.CameraAccessException;
import android.hardware.camera2.CameraManager;
import android.os.Build;
import android.os.Bundle;
import android.view.View;
import android.widget.CompoundButton;
import android.widget.Toast;
import android.widget.ToggleButton;

public class MainActivity extends Activity {

    ToggleButton tb;
    CameraManager cm;
    String cid;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        tb = (ToggleButton) findViewById(R.id.toggleButton);
        tb.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view) {
                if (tb.getTextOff().equals("ON")){
                        tb.setTextOff("OFF");
                }else {
                        tb.setTextOff("ON");
                }
            }
        });
    }
}