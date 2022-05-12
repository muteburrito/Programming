package com.example.event;

import androidx.appcompat.app.AppCompatActivity;

import android.app.Activity;
import android.app.DatePickerDialog;
import android.app.TimePickerDialog;
import android.graphics.Color;
import android.os.Bundle;
import android.text.format.DateFormat;
import android.view.MotionEvent;
import android.view.View;
import android.widget.Button;
import android.widget.DatePicker;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.TimePicker;
import android.widget.Toast;

import java.util.Calendar;

public class MainActivity extends Activity {
    TextView textView;
    Button button;
    EditText fd,td,ft,tt,event,subject;
    int day, month, year, hour, minute;
    Calendar calendar;
    TimePickerDialog timePickerDialog;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        event = (EditText) findViewById(R.id.eventName);
        subject = (EditText) findViewById(R.id.subject);
        fd = (EditText) findViewById(R.id.fromDate);
        td = (EditText) findViewById(R.id.toDate);
        ft = (EditText) findViewById(R.id.fromTime);
        tt = (EditText) findViewById(R.id.toTime);
        button = (Button) findViewById(R.id.ok);

        fd.setOnTouchListener(new View.OnTouchListener() {
            @Override
            public boolean onTouch(View view, MotionEvent motionEvent) {
                calendar = Calendar.getInstance();
                year = calendar.get(Calendar.YEAR);
                month = calendar.get(Calendar.MONTH);
                day = calendar.get(Calendar.DAY_OF_MONTH);

                DatePickerDialog picker = new DatePickerDialog(MainActivity.this, new DatePickerDialog.OnDateSetListener() {

                    @Override
                    public void onDateSet(DatePicker datePicker, int year, int month, int day) {
                        fd.setText(day + "/" + (month + 1) + "/" + year);
                    }
                }, year, month, day);
                picker.show();
                return true;
            }
        });
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (event.getText().toString().isEmpty() || subject.getText().toString().isEmpty())
                    Toast.makeText(MainActivity.this, "Please insert Event Name and Subject", Toast.LENGTH_SHORT).show();
                else if (fd.getText().toString().isEmpty() || ft.getText().toString().isEmpty() || td.getText().toString().isEmpty() || tt.getText().toString().isEmpty()) {
                    Toast.makeText(MainActivity.this, "Please select date and  time", Toast.LENGTH_SHORT).show();
                }else Toast.makeText(MainActivity.this, "Event inserted successfully", Toast.LENGTH_SHORT).show();
            }
        });

        td.setOnTouchListener(new View.OnTouchListener() {
            @Override
            public boolean onTouch(View view, MotionEvent motionEvent) {
                calendar = Calendar.getInstance();
                year = calendar.get(Calendar.YEAR);
                month = calendar.get(Calendar.MONTH);
                day = calendar.get(Calendar.DAY_OF_MONTH);

                if (fd.getText().toString().isEmpty()) return true;

                DatePickerDialog picker = new DatePickerDialog(MainActivity.this, new DatePickerDialog.OnDateSetListener() {

                    @Override
                    public void onDateSet(DatePicker datePicker, int year, int month, int day) {
                        td.setText(day+"/"+(month+1)+"/"+year);
                    }
                }, year, month,day+1);
                picker.show();
                return true;
            }
        });

        ft.setOnTouchListener(new View.OnTouchListener() {
            @Override
            public boolean onTouch(View view, MotionEvent motionEvent) {
                calendar = Calendar.getInstance();
                hour = calendar.get(Calendar.HOUR_OF_DAY);
                minute = calendar.get(Calendar.MINUTE);

                timePickerDialog = new TimePickerDialog(MainActivity.this, new TimePickerDialog.OnTimeSetListener()
                {
                    @Override
                    public void onTimeSet(TimePicker timePicker, int hour, int min) {
                        ft.setText(hour+":"+min);
                    }
                },hour,minute,false);
                timePickerDialog.show();
                return true;
            }
        });

        tt.setOnTouchListener(new View.OnTouchListener() {
            @Override
            public boolean onTouch(View view, MotionEvent motionEvent) {
                calendar = Calendar.getInstance();
                hour = calendar.get(Calendar.HOUR_OF_DAY);
                minute = calendar.get(Calendar.MINUTE);

                if (ft.getText().toString().isEmpty()) return false;

                TimePickerDialog timePickerDialog = new TimePickerDialog(MainActivity.this, new TimePickerDialog.OnTimeSetListener()
                {
                    @Override
                    public void onTimeSet(TimePicker timePicker, int hour, int min) {
                        tt.setText(hour+":"+min);
                    }
                },12,00,false);
                timePickerDialog.show();
                return true;
            }
        });
    }
}