package com.onwardsmg.logcattest;

import android.app.Application;

import com.onwardsmg.logtoy.LogToy;

public class MyApplication extends Application {

    @Override
    public void onCreate() {
        super.onCreate();
        LogToy.init(getApplicationContext());
    }
}
