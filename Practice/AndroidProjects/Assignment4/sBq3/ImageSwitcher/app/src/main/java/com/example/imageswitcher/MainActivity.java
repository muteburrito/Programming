package com.example.imageswitcher;

import androidx.appcompat.app.AppCompatActivity;

import android.app.ActionBar;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.Button;
import android.widget.ImageSwitcher;
import android.widget.ImageView;
import android.widget.Toast;
import android.widget.ViewSwitcher;

import java.lang.annotation.Annotation;

public class MainActivity extends AppCompatActivity {

    Button b;
    ImageSwitcher sw;
//    String language[] = {"R.mipmap.c_foreground", "R.mipmap.cpp_foreground", "R.mipmap.java_foreground", "R.mipmap.python_foreground"};
    int i = 1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        b = (Button) findViewById(R.id.Button);
        Animation in = AnimationUtils.loadAnimation(this, android.R.anim.slide_in_left);
        Animation out = AnimationUtils.loadAnimation(this, android.R.anim.slide_out_right);
        sw = (ImageSwitcher) findViewById(R.id.imageSwitcher);
        sw.setInAnimation(in);
        sw.setOutAnimation(out);
        sw.setFactory(new ViewSwitcher.ViewFactory() {
            @Override
            public View makeView() {
                ImageView myView = new ImageView(getApplicationContext());
                return myView;
            }
        });
        b.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                switch(i){
                    case 1 : sw.setImageResource(R.mipmap.c_foreground);
                            break;
                    case 2 : sw.setImageResource(R.mipmap.cpp_foreground);
                        break;
                    case 3 : sw.setImageResource(R.mipmap.java_foreground);
                        break;
                    case 4: sw.setImageResource(R.mipmap.python_foreground);
                        break;
                }
                i++;
                if (i==5)
                    i=0;
            }
        });
    }
}


