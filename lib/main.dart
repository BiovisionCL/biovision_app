import 'package:flutter/material.dart';
import 'features/home/presentation/home_page.dart';

void main() {
  runApp(const BiovisionApp());
}

class BiovisionApp extends StatelessWidget {
  const BiovisionApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Biovision',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.green),
        useMaterial3: true,
      ),
      home: const HomePage(),
    );
  }
}
