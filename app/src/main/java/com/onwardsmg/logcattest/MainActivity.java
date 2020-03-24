package com.onwardsmg.logcattest;

import android.os.Bundle;
import android.os.SystemClock;

import androidx.appcompat.app.AppCompatActivity;

import com.onwardsmg.logtoy.LogToy;

public class MainActivity extends AppCompatActivity {

    private long time;
    private boolean isDestroy;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        time = SystemClock.currentThreadTimeMillis();

        new Thread() {
            @Override
            public void run() {
                while (!isDestroy) {
                    time += 1000;
                    SystemClock.sleep(1000);
                    LogToy.d("bigbang", "测试中文 time is: " + time);
                }
            }
        }.start();
    }

    @Override
    protected void onDestroy() {
        isDestroy = true;
        LogToy.destory();
        super.onDestroy();
    }
}
