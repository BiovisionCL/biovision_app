import 'package:flutter/material.dart';

final ThemeData appTheme = ThemeData(
  primaryColor: const Color(0xFF0B3D91),
  scaffoldBackgroundColor: Colors.white,
  fontFamily: 'sans-serif',
  textTheme: const TextTheme(
    titleLarge: TextStyle(fontSize: 20, fontWeight: FontWeight.w600, color: Colors.black87),
  ),
  appBarTheme: const AppBarTheme(
    backgroundColor: Colors.white,
    iconTheme: IconThemeData(color: Color(0xFF0B3D91)),
    titleTextStyle: TextStyle(fontSize: 24, fontWeight: FontWeight.bold, color: Color(0xFF0B3D91)),
  ),
);