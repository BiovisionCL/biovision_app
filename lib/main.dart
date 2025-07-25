import 'package:flutter/material.dart';
import 'shared/theme.dart';
import 'features/home/presentation/home_page.dart';

void main() {
  runApp(const BiovisionApp());
}

class BiovisionApp extends StatelessWidget {
  const BiovisionApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Biovision Modular',
      theme: appTheme,
      home: const HomePage(),
    );
  }
}