package com.example.activitylifecycle;

import android.app.Activity;
import android.util.Log;
import android.os.Bundle;

public class MainActivity extends Activity {
    String tag = "Events";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        Log.d(tag,"In on Create Event");
        setContentView(R.layout.activity_main);
    }
    @Override
    public void onStart(){
        super.onStart();
        Log.d(tag,"In the onStart() event");
    }
    @Override
    public void onRestart(){
        super.onRestart();
        Log.d(tag,"In the onRestart() event");
    }
    @Override
    public void onResume(){
        super.onResume();
        Log.d(tag,"In the onResume() event");
    }
    public void onStop(){
        super.onStop();
        Log.d(tag,"In the onStop() event");
    }
    public void onDestroy(){
        super.onDestroy();
        Log.d(tag,"In the onDestroy() event");
    }
}