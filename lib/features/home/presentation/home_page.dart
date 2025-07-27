
import 'package:flutter/material.dart';
import '../../../core/widgets/primary_button.dart';

class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      _counter++;
    });
    print("Botón presionado");
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Home")),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text('$_counter', style: Theme.of(context).textTheme.headlineMedium),
            const SizedBox(height: 20),
            PrimaryButton(
              text: "Presióname",
              onPressed: _incrementCounter,
            ),
          ],
        ),
      ),
    );
  }
}
