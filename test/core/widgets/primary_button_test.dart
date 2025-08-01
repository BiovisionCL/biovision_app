// @dart=2.17
// @dart=2.17

import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:biovision_app/core/widgets/primary_button.dart'; // Ajusta ruta si es necesario

void main() {
  testWidgets('PrimaryButton renders with given text', (WidgetTester tester) async {
    await tester.pumpWidget(
      MaterialApp(
        home: Scaffold(
          body: PrimaryButton(
            text: 'Click Me',
            onPressed: () {},
          ),
        ),
      ),
    );

    expect(find.text('Click Me'), findsOneWidget);
  });
}
